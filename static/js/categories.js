$(function () {
    var CategoriesView = function () {
        this.columns = 4;
        this.columnWidth = undefined;

        this.$categories = $('.categories');
        this.$container = this.$categories.find('.container');
        this.$columns = this.$container.find('.columns');

        this.$left = this.$categories.find('.left');
        this.$right = this.$categories.find('.right');

        this.init();
    };

    CategoriesView.prototype = {
        init: function () {
            this.bindEvents();
            this.resize();
        },

        bindEvents: function () {
            var _this = this;

            $(window).on('resize', function () {
                _this.resize();
            });

            this.$left.add(this.$right).on('click', function () {
                _this.setMarginLeft(($(this).hasClass('left') ? '+' : '-') + '=' + _this.columnWidth + 'px');
            });

            this.$categories.on('click', 'li', function () {
                _this.openCategory($(this));
            });

            this.$categories.on('click', '.open', function (e) {
                e.stopPropagation();
            });
        },

        openCategory: function ($item) {
            var _this = this,
                $category = $item.closest('ul'),
                $newCategory,
                currentLevel = parseInt($category.attr('data-level'));

            this.loadChilds($item.attr('data-id'), function (childs) {
                $category.nextAll().remove();
                $category.find('li.active').removeClass('active');
                $item.addClass('active');

                $newCategory = $(childs).attr('data-level', currentLevel + 1).css('width', _this.columnWidth);
                if (!$newCategory.find('li').length) {
                    return;
                }

                _this.$columns.append($newCategory);
                _this.setMarginLeft(
                    - (currentLevel + 2 > _this.columns ? _this.columnWidth * ((currentLevel + 2) - _this.columns) : 0)
                );
            });
        },

        getHiddenLeftColumnsCount: function () {
            return parseInt(this.getMarginLeft() / this.columnWidth);
        },

        getMarginLeft: function () {
            return Math.abs(parseFloat(this.$columns.css('margin-left')));
        },

        setMarginLeft: function (value) {
            this.$columns.animate({'margin-left': value}, $.proxy(this.updateControls, this));
        },

        updateControls: function () {
            var columnsCount = this.$columns.find('> ul').length,
                hiddenLeftColumnsCount = this.getHiddenLeftColumnsCount();

            this.$left.toggle(hiddenLeftColumnsCount > 0);
            this.$right.toggle(this.columns + hiddenLeftColumnsCount < columnsCount);
        },

        loadChilds: function (parent, callback) {
            $.ajax({
                type: 'GET',
                url: '/category/level',
                data: {
                    parent: parent
                },
                callback: callback
            });
        },

        resize: function () {
            this.columnWidth = this.$categories.width() / this.columns;
            this.$columns.find('> ul').width(this.columnWidth);
            this.setMarginLeft(- this.getHiddenLeftColumnsCount() * this.columnWidth);
        }
    };

    new CategoriesView();
});