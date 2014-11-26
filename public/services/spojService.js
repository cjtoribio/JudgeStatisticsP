angular.module('JudgeStatsApp')
  .factory('Spoj', function($resource) {
    return {
    	getSubmissions : function(handle, callback) {
    		$resource('/spoj/subs/:id').query({
    			id: handle,
    		}, callback);
		},
    	getStats : function(handle, callback) {
    		$resource('/spoj/stats/:id').get({
    			id: handle,
    		}, callback);
		}
    };
  });