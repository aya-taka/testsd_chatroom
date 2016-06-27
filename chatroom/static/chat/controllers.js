var TodoControllers = angular.module('TodoControllers', []);

TodoControllers.controller('TodoListCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.todoItems = [];
    $scope.resistRoomList = [];
    $scope.todoList = "";
    $scope.roomId = 1;
    $scope.channel = 'comments';
    /*
    $dragon.onReady(function() {
        $dragon.subscribe('comment-route', $scope.channel, {}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getSingle('user-route', {}).then(function(response) {
            // console.log(response.data.id);
            $scope.user = response.data.id;
        });
        $dragon.getSingle('room-route', {id:$scope.roomId}).then(function(response) {
            $scope.todoList = response.data;
        });
        $dragon.getList('comment-route', {room_id:$scope.roomId}).then(function(response) {
            for (var i=0;i<response.data.length;i++){
                response.data[i].room = $scope.roomId;
            }
            $scope.todoItems = response.data;
        });
    });
    */
    $dragon.onChannelMessage(function(channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function() {
                $scope.dataMapper.mapData($scope.todoItems, message);
            });
        }
    });

    $scope.dataadd = function(data) {
        // console.log($scope.user);
        // console.log($scope.roomId);
        // data.room = $scope.todoList;
        $dragon.create('comment-route', {text:data.text, room:$scope.roomId});
        data.text = "";
        $dragon.getSingle('regist-route', {room_id:$scope.roomId}).then(function(response) {
            $scope.resistRoomList = response.data;
            // console.log($scope.resistRoomList.room);
        });
       // console.log($scope.todoList.id);
    }

    $scope.setRoomId = function(room) {
        // console.log(room);
        $scope.roomId = room.number;

        $dragon.subscribe('comment-route', $scope.channel, {}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });
        $dragon.getSingle('user-route', {}).then(function(response) {
            // console.log(response.data);
            $scope.user = response.data;
        });
        $dragon.getSingle('regist-route', {room_id:$scope.roomId}).then(function(response) {
            $scope.resistRoomList = response.data;
            // console.log($scope.resistRoomList.room);
        });
        $dragon.getSingle('room-route', {id:$scope.roomId}).then(function(response) {
            $scope.todoList = response.data;
        });
        $dragon.getList('comment-route', {room_id:$scope.roomId}).then(function(response) {
            $scope.todoItems = response.data;
        });
        // console.log($scope.roomId);
    }

    $scope.datacreate = function(roomname, roomdes) {
        // console.log($scope.user);
        $dragon.create('room-route', {name:roomname.text, des:roomdes.text});
        roomname.text = "";
        roomdes.text = "";
    }

    $scope.datadelete = function(item) {
        $dragon.delete('comment-route', item);
    }
}]);