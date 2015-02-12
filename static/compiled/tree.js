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

var TreeCategoryItems = React.createClass({displayName: "TreeCategoryItems",
		render: function () {
			var treeCategory = this.props.treeCategory,
				open = treeCategory.state.open;

			return (
				React.createElement("div", null, 
					React.createElement("i", {style: Styles('tree.item.icon.' + (open ? 'collapse' : 'expand'))}, 
						open ? '-' : '+'
					), 

					React.createElement("div", {style: Styles(open ? 'show' : 'hide')}, 
						treeCategory.state.items
					)
				)
			);
		}
	}),

	TreeCategory = React.createClass({displayName: "TreeCategory",
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
				return React.createElement(TreeCategory, {
						 tree: this.props.tree, 
						 key: item.id, 
						 id: item.id, 
						 name: item.name});
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
				React.createElement("div", {style: Styles('tree.item'), onClick: this.toggle}, 
					this.props.name, 

					React.createElement("div", {style: Styles('tree.actions')}, 
						React.createElement("a", {onClick: this.toggleAddCategory}, 
							React.createElement("i", {className: "fa fa-plus-circle"}), " Dodaj podkategorię"
						)
					), 

					React.createElement(Display, {when: this.state.addingCategory}, 
						React.createElement(TreeCategoryNew, {category: this})
					), 

					React.createElement(Display, {when: this.state.items.length}, 
						React.createElement(TreeCategoryItems, {treeCategory: this})
					)
				)
			);
		}
	}),

	TreeCategoryNew = React.createClass({displayName: "TreeCategoryNew",
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
						React.createElement(TreeCategory, {
							tree: _this.props.category.props.tree, 
							key: response.id, 
							id: response.id, 
							name: _this.state.name})
					);
				}
			});
		},

		render: function () {
			return (
				React.createElement("div", {style: Styles('tree.addCategory')}, 
					React.createElement("input", {type: "text", onClick: this.preventClickEvent, onChange: this.changeName}), 
					React.createElement("button", {onClick: this.add}, "Dodaj")
				)
			);
		}
	}),

	Tree = React.createClass({displayName: "Tree",
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
				React.createElement("div", {style: Styles('tree')}, 
					React.createElement(TreeCategory, {tree: this, name: this.props.name})
				)
			);
		}
	});