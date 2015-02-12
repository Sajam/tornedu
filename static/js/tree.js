Styles('tree', {
	border: '1px solid #ccc',
	padding: 5,

	item: {
		position: 'relative',
		paddingLeft: 15,

		icon: {
			position: 'absolute',
			top: 0,
			left: 0,

			expand: {
				_extend: true
			},

			collapse: {
				_extend: true
			}
		}
	},

	actions: {
		display: 'inline-block',
		fontSize: 12,
		marginLeft: 10
	}
});

var TreeCategoryItems = React.createClass({
		render: function () {
			var treeCategory = this.props.treeCategory,
				open = treeCategory.state.open;

			return (
				<div>
					<i style={Styles('tree.item.icon.' + (open ? 'collapse' : 'expand'))}>
						{open ? '-' : '+'}
					</i>

					<div style={Styles(open ? 'show' : 'hide')}>
						{treeCategory.state.items}
					</div>
				</div>
			);
		}
	}),

	TreeCategory = React.createClass({
		getInitialState: function () {
			return {
				open: true,
				addingCategory: false,
				items: []
			}
		},

		getDefaultProps: function () {
			return {
				id: undefined,
				name: 'Root'
			};
		},

		componentWillMount: function () {
			this.state.items = this.props.tree.getItemsForCategory(this.props.id).map(function (item) {
				return <TreeCategory
						 tree={this.props.tree} 
						 key={item.id}
						 id={item.id}
						 name={item.name} />;
			}, this);
		},

		toggle: function (e) {
			e.stopPropagation();

			this.setState({
				open: !this.state.open
			});
		},

		toggleAddCategory: function (e) {
			e.stopPropagation();

			this.setState({
				addingCategory: !this.state.addingCategory
			});
		},

		render: function () {
			return (
				<div style={Styles('tree.item')} onClick={this.toggle}>
					{this.props.name}

					<div style={Styles('tree.actions')}>
						<a onClick={this.toggleAddCategory}>
							<i className="fa fa-plus-circle"></i> Dodaj podkategorię
						</a>
					</div>

					<Display when={this.state.addingCategory}>
						<TreeCategoryNew category={this} />
					</Display>

					<Display when={this.state.items.length}>
						<TreeCategoryItems treeCategory={this} />
					</Display>
				</div>
			);
		}
	}),

	TreeCategoryNew = React.createClass({
		mixins: [BasicMixins],

		getInitialState: function () {
			return {
				name: ''
			};
		},

		changeName: function (e) {
			this.setState({name: e.target.value});
		},

		add: function (e) {
			var _this = this;

			$.ajax({
				type: 'POST',
				url: '/admin/category/add',
				async: false,
				data: {
					name: this.state.name,
					parent: this.props.category.props.id
				},
				success: function (response) {
					response = JSON.parse(response);

					_this.props.category.state.items.push(
						<TreeCategory
							tree={_this.props.category.props.tree}
							key={response.id}
							id={response.id}
							name={_this.state.name} />
					);
				}
			});
		},

		render: function () {
			return (
				<div style={Styles('tree.addCategory')}>
					<input type="text" onClick={this.preventClickEvent} onChange={this.changeName} />
					<button onClick={this.add}>Dodaj</button>
				</div>
			);
		}
	}),

	Tree = React.createClass({
		propTypes: {
			data: React.PropTypes.array
		},

		getDefaultProps: function () {
			return {
				name: 'Root'
			};
		},

		getItemsForCategory: function (categoryId) {
			return this.props.data.filter(function (item) {
				return item.parent === categoryId;
			});
		},

		render: function () {
			return (
				<div style={Styles('tree')}>
					<TreeCategory tree={this} name={this.props.name} />
				</div>
			);
		}
	});