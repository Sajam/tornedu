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
                // Use same properties as in icon.
				_extend: true
			},

			collapse: {
                // Use same properties as in icon.
				_extend: true
			}
		}
	},

	actions: {
		fontSize: 12,
		marginLeft: 10,

        a: {
            marginRight: 10
        }
	}
});

var TreeCategory = React.createClass({displayName: "TreeCategory",
        statics: {
            defaultName: '(blank)'
        },

		getDefaultProps: function () {
			return {
				id: undefined,
                parent: undefined,
				name: '(blank)'
			};
		},

        getInitialState: function () {
			return {
				open: true,
                hover: false
			}
		},

        componentDidMount: function () {
            $(this.getDOMNode()).on('mouseenter mouseleave', function (e) {
                this.setState({hover: e.type === 'mouseenter'});
            }.bind(this));
        },

		toggleCategory: function (e) {
			e.stopPropagation();
			this.setState({open: !this.state.open});
		},

		addSubcategory: function (e) {
			e.stopPropagation();

            var _this = this,
                name = prompt('Enter name:');

            name = name && name.trim().length ? name : TreeCategory.defaultName;

            $.ajax({
				type: 'POST',
				url: '/admin/category/add',
				data: {
					name: name,
					parent: this.props.id
				},
				success: function (response) {
					response = JSON.parse(response);

					_this.props.tree.props.data.push({
                        id: response.id,
                        name: name,
                        parent: _this.props.id
                    });

                    _this.forceUpdate();
				}
			});
		},

        changeCategoryName: function (e) {
            e.stopPropagation();

            var _this = this,
                newName = prompt('Enter name:', this.props.name);

            if (newName) {
                newName = newName.trim();
                newName = newName.length ? newName : TreeCategory.defaultName;

                $.ajax({
                    type: 'POST',
                    url: '/admin/category/edit',
                    data: {
                        id: _this.props.id,
                        name: newName
                    },
                    success: function (response) {
                        var categoryDataIndex = _this.props.tree.getIndexByCategoryId(_this.props.id);

                        _this.props.tree.props.data[categoryDataIndex].name = newName;
                        _this.forceUpdate();
                    }
                });
            }
        },

        deleteCategory: function (e) {
            var _this = this;

            $.ajax({
                type: 'POST',
                url: '/admin/category/delete',
                data: {
                    id: this.props.id
                },
                success: function (response) {
                    var categoryDataIndex = _this.props.tree.getIndexByCategoryId(_this.props.id);

                    delete _this.props.tree.props.data[categoryDataIndex];
                    _this.props.tree.props.data.splice(categoryDataIndex, 1);
                    _this.props.parent.forceUpdate();
                }
            });
        },

		render: function () {
            var categories = this.props.tree.getItemsForCategory(this.props.id).map(function (category) {
				return Tree.createCategory(this.props.tree, this, category.id, category.name);
			}, this);

			return (
				React.createElement("div", {style: Styles('tree.item'), onClick: this.toggleCategory}, 
					this.props.name, 

                    React.createElement(Display, {inline: true, when: this.state.hover}, 
					    React.createElement("div", {style: Styles('tree.actions')}, 
                            React.createElement("a", {style: Styles('tree.actions.a'), onClick: this.addSubcategory}, 
                                React.createElement("i", {className: "fa fa-plus-circle"}), " Dodaj podkategorię"
                            ), 
                            React.createElement(Display, {inline: true, when: this.props.parent}, 
                                React.createElement("a", {style: Styles('tree.actions.a'), onClick: this.changeCategoryName}, 
                                    React.createElement("i", {className: "fa fa-pencil"}), " Zmień nazwę"
                                ), 
                                React.createElement("a", {style: Styles('tree.actions.a'), onClick: this.deleteCategory}, 
                                    React.createElement("i", {className: "fa fa-times"}), " Usuń kategorię"
                                )
                            )
					    )
                    ), 

					React.createElement(Display, {when: categories.length}, 
                        React.createElement("div", null, 
                            React.createElement("i", {style: Styles('tree.item.icon.' + (this.state.open ? 'collapse' : 'expand'))}, 
                                this.state.open ? '-' : '+'
                            ), 

                            React.createElement("div", {style: Styles(this.state.open ? 'show' : 'hide')}, 
                                categories
                            )
                        )
					)
				)
			);
		}
	}),

	Tree = React.createClass({displayName: "Tree",
        statics: {
            createCategory: function (tree, parent, id, name) {
                return React.createElement(TreeCategory, {
                    tree: tree, 
                    parent: parent, 
                    id: id, 
                    name: name, 
                    key: id}
                )
            }
        },

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

        getIndexByCategoryId: function (id) {
            var i, length;

            for (i = 0, length = this.props.data.length; i < length; i += 1) {
                if (id === this.props.data[i].id) {
                    return i;
                }
            }
        },

		render: function () {
			return (
				React.createElement("div", {style: Styles('tree')}, 
                    Tree.createCategory(this, undefined, undefined, this.props.name)
				)
			);
		}
	});