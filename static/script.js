$(function() {
	
	// Filter
	$("button[cs-filter]").click(function() {
		var t = $(this).attr('cs-filter');
		$("button[cs-filter]").removeClass('btn-active');
		$(this).addClass('btn-active');
		if (t == "*") {
			$("li.items[cs-category]").show("fast");
		} else {
			$.each($("li.items[cs-category]"), function(index, value) {
				if (!$(this).attr('cs-category').match(new RegExp(t))) {
					$(this).hide("fast");
				} else {
					$(this).show("fast");
				}
			});
		}
	});
	
	// Sort Button
	$("button[cs-sort]").click(function() {
		var t = $(this).attr('cs-sort');
		$("button[cs-sort]").removeClass('btn-active');
		$(this).addClass('btn-active');
		switch (t) {
			case 'price':
				$("ul li.items").sort(function(a, b) {
					var f = parseInt($(b).find('span.product-price').text().replace(',', ''));
					var s = parseInt($(a).find('span.product-price').text().replace(',', ''));
					return (f < s) ? 1 : -1;
				}).each(function() {
					var elem = $(this);
					elem.remove();
					$(elem).appendTo("ul");
				});
				break;

			case 'name':
				$("ul li.items").sort(function(a, b) {
					return (($(b).find('span.product-name').text()) < ($(a).find('span.product-name').text())) ? 1 : -1;
				}).appendTo('ul');
				break;
		}
	});
	
	// Slider Start
	var count = $("#cs-image-slider > div").length;
	var slider = 1
	var speed = 5000
	var fadeSpeed = 300
	var loop
	start()
	$("#1").fadeIn(fadeSpeed);
	$('.right').click(right)
	$('.left').click(left)
	$('#slider').hover(stop, start)

	function start() {
		loop = setInterval(next, speed)
	}

	function stop() {
		clearInterval(loop)
	}

	function right() {
		stop()
		next()
		start()
		return false
	}

	function left() {
		stop()
		prev()
		start()
		return false
	}

	function prev() {
		slider--
		if (slider < 1) {
			slider = count
		}

		$("#cs-image-slider > div").fadeOut(fadeSpeed)
		$("#" + slider).fadeIn(fadeSpeed)
	}

	function next() {
		slider++
		if (slider > count) {
			slider = 1
		}

		$("#cs-image-slider > div").fadeOut(fadeSpeed)
		$("#" + slider).fadeIn(fadeSpeed)
	}
});