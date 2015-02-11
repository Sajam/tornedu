var Styles = function () {
	// Basic styles definitions can go below.
	var styles = {
		show: {
			display: 'block'
		},

		hide: {
			display: 'none'
		}
	},

	getStyle = function (styleName) {
		var result = {},
			stylePathParts = styleName.split('.'),
			currentStylesLocation = styles, previousStylesLocation,
			propertiesToMerge = [],
			propertyName, i = 0, length = stylePathParts.length;

		while (i < length) {
			if (!currentStylesLocation.hasOwnProperty(stylePathParts[i])) {
				return {};
			}

			if (i !== 0 && currentStylesLocation[stylePathParts[i]].hasOwnProperty('_extend') &&
					currentStylesLocation[stylePathParts[i]]['_extend'] === true) {
				propertiesToMerge.push(previousStylesLocation[stylePathParts[i - 1]]);
			}
			
			previousStylesLocation = currentStylesLocation;
			currentStylesLocation = currentStylesLocation[stylePathParts[i]];
			
			i += 1;
		}

		if (i === length) {
			propertiesToMerge.push(currentStylesLocation);

			for (i = 0, length = propertiesToMerge.length; i < length; i += 1) {
				for (propertyName in propertiesToMerge[i]) {
					if (propertyName !== '_extend' &&
							Object.prototype.toString.call(propertiesToMerge[i][propertyName]) != '[object Object]') {
						result[propertyName] = propertiesToMerge[i][propertyName];
					}
				}
			}
		}

		return result;
	},

	setStyle = function (styleName, styleValues) {
		if (styleName.indexOf('.') === -1) {
			styles[styleName] = styleValues;
		} else {
			// Path specified using dot-notation.
		}
	};

	// CSS('one_arg') -> get styles, CSS('two', {ar: gs}) -> set styles
	return function (styleName, styleValues) {
		return (arguments.length < 2) ? getStyle(styleName) : setStyle(styleName, styleValues);
	};
}();