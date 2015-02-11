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
						treeCategory.props.items
					)
				)
			);
		}
	}),

	TreeCategory = React.createClass({displayName: "TreeCategory",
		getInitialState: function () {
			return {
				open: true
			}
		},

		getDefaultProps: function () {
			return {
				id: undefined,
				name: 'Root'
			};
		},

		componentWillMount: function () {
			this.props.items = this.props.tree.getItemsForCategory(this.props.id).map(function (item) {
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

		render: function () {
			return (
				React.createElement("div", {style: Styles('tree.item'), onClick: this.toggle}, 
					this.props.name, 

					React.createElement(Display, {when: this.props.items.length}, 
						React.createElement(TreeCategoryItems, {treeCategory: this})
					)
				)
			);
		}
	}),

	Tree = React.createClass({displayName: "Tree",
		propTypes: {
			data: React.PropTypes.array
		},

		getItemsForCategory: function (categoryId) {
			return this.props.data.filter(function (item) {
				return item.parent === categoryId;
			});
		},

		render: function () {
			return (
				React.createElement("div", {style: Styles('tree')}, 
					React.createElement(TreeCategory, {tree: this})
				)
			);
		}
	});