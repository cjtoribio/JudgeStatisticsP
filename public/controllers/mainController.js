angular.module('JudgeStatsApp')
.controller(
	'MainController', 
	function($scope, $alert, LoginService, $rootScope, $location, LoginService) {
		$scope.logOut = function() {
			LoginService.logOut();
			$location.path("/login");
		}
	}
);