angular.module('JudgeStatsApp')
  .factory('Spoj', function($resource) {
    return {
    	getSubmissions : function(handle, callback) {
    		$resource('/spoj/subs/:id').query({
    			id: 1,
    		}, callback);
		},
    	getStats : function(handle, callback) {
    		$resource('/spoj/stats/:id').get({
    			id: 1,
    		}, callback);
		}
    };
  });