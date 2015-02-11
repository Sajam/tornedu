var Display = React.createClass({
	render: function () {
		if (!!(this.props.when) === true) {
			return (
				<div>
					{this.props.children}
				</div>
			);
		}

		return false;
	}
});