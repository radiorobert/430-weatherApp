var FutureWeather = angular.module('FutureWeather',[]);

FutureWeather.controller('testing',function($scope){
	var socket = io.connect('http://' + document.domain + ':' + location.port);

	$scope.address = "testAddress",
	$scope.date = "testDate",
	$scope.results = [],

	$scope.makeForecast = function() {
		socket.emit('makeForecast', $scope.address, $scope.date);
	};

	socket.on('connect', function() {
		console.log('Connected to main');
	});

	socket.on('print_input', function(data){
		$scope.results.push(data[0]);
		$scope.results.push(data[1]);

		$scope.$apply()

	});
