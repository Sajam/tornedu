Styles('display', {
	inline: {
		display: 'inline'
	},

	block: {
		display: 'block'
	}
});

var Display = React.createClass({
	getDefaultProps: function () {
		return {
			inline: false
		};
	},

	render: function () {
		if (!!(this.props.when) === true) {
			return (
				<div style={Styles(this.props.inline ? 'inline' : 'block')}>
					{this.props.children}
				</div>
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