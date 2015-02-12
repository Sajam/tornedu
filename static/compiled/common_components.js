Styles('display', {
	inline: {
		display: 'inline'
	},

	block: {
		display: 'block'
	}
});

var Display = React.createClass({displayName: "Display",
	getDefaultProps: function () {
		return {
			inline: false
		};
	},

	render: function () {
		if (!!(this.props.when) === true) {
			return (
				React.createElement("div", {style: Styles(this.props.inline ? 'inline' : 'block')}, 
					this.props.children
				)
			);
		}

		return false;
	}
});

var BasicMixins = {
	preventClickEvent: function (e) {
		e.stopPropagation();
	}
};