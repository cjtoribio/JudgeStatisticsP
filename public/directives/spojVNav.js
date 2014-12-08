angular.module('JudgeStatsApp').directive('spojVNav', function() {
	return {
        replace: true,
        transclude: true,
		remove: true,
		templateUrl : 'templates/spojVNav.html'
	}
});