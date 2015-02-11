var Display = React.createClass({displayName: "Display",
	render: function () {
		if (!!(this.props.when) === true) {
			return (
				React.createElement("div", null, 
					this.props.children
				)
			);
		}

		return false;
	}
});