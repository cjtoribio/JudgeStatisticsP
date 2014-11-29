angular.module('JudgeStatsApp').directive('messages', function() {
	return {
		remove: true,
		template: ' <div style="position:fixed;right:20px; bottom:20px;">' +
				  '		<div style="background-color:#fff;width:300px;padding:10px 20px; margin:5px;border-radius:5px;box-shadow:0px 0px 2px 0px #aaa;" ng-repeat="x in msgs">{{x.message}}</div>' +
				  ' </div>',
		scope: {},
		controller: function($scope, MessageService){
			$scope.msgs = MessageService.msgs;
		}
	}
});