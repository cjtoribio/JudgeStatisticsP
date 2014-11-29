angular.module('JudgeStatsApp')
.factory('MessageService', function($timeout) {
	var service = {};
	service.msgs = {};
	service.id = 1;
	service.getId = function(){
		var tmp = service.id;
		service.id = tmp+1;
		return tmp;
	}
	service.post = function(msgOptions){
		var id = service.getId();
		service.msgs[id] = {
			message: msgOptions.message,
			id: id
		};
		console.log('added: ' + msgOptions.message);
		if(msgOptions.timeout){
			$timeout(function(){
				delete service.msgs[id];
				console.log('removed: ' + msgOptions.message);
			}, msgOptions.timeout);
		};
	};
	return service;
});