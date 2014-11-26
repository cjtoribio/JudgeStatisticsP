angular.module('JudgeStatsApp').controller('SpojController',
		function($scope, $alert, Spoj) {
			$scope.handle = '';
			$scope.handles = [];
			$scope.submissions = {};
			$scope.veredicts = [ 'AC', 'WA', 'TLE', 'RE' ];
			$scope.submit = function() {
				Spoj.getSubmissions($scope.handle, function(data){
					angular.forEach(data , function(sub, index){
						sub.submissionDate = new Date(sub.submissionDate);
						sub.insertDate = new Date(sub.insertDate);
					});
					$scope.subs = data;
				});
				Spoj.getStats($scope.handle, function(data){
					data.lastSubmission = new Date(data.lastSubmission);
					$scope.stats = data;
					$scope.data.data[0].y = [];
					$scope.data.data[0].tooltip = [];
					angular.forEach($scope.data.series , function(ser , idx){
						$scope.data.data[0].y.push(data.veredictMap[ser]);
						$scope.data.data[0].tooltip.push(data.veredictMap[ser]);
					});
				});
			};

			$scope.viewedSubs = [];
			$scope.subs = []

			$scope.config = {
					  title: '',
					  tooltips: true,
					  labels: false,
					  mouseover: function() {},
					  mouseout: function() {},
					  click: function(a,b) {
						  console.log(a);
					  },
					  legend: {
					    display: true,
					    //could be 'left, right'
					    position: 'right'
					  },
					  colors: ['#0A0','red','yellow','orange','gray'],
					  innerRadius: 0, // applicable on pieCharts, can be a percentage like '50%'
					  lineLegend: 'lineEnd' // can be also 'traditional'
					};
			
			$scope.data = {
				    series: ['AC', 'WA', 'TLE', 'RE', 'CE', '--'],
				    data: [{
				      x: "TotalProblems",
				      y: [0,0,0,0,0,0],
				      tooltip: [1,2,3,4,5]
				    }]
			};
			
		});