angular.module('JudgeStatsApp')
.controller(
	'LoginController', 
	function($scope, $alert, LoginService, $rootScope, $location, MessageService) {
		$scope.authData = LoginService.authData;
		$scope.credentials = {};
		$scope.login = function(credentials){
			LoginService.login(credentials, function(data){
				if($scope.authData.isOnline){
					$location.path('/spoj/stats');
				}else{
					var opts = {timeout: 1000};
					if(data.status == 'UNotFound')
						opts.message = 'User not found';	
					else if(data.status == 'IncPass')
						opts.message = 'Incorrect password';
					else
						opts.message = 'Cannot login at this moment';
					MessageService.post(opts);
				}
			});
		};

		$scope.logOut = function(){
			LoginService.logOut();
		}

		$scope.verifyToken = function(){
			LoginService.verifyToken(function(data, status){
				if(data != null)
					$scope.response = data.response;
				else
					$scope.response = "Not authorized";
			});
		}
	}
);