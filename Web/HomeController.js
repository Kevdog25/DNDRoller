"use strict";
var HomeController = /** @class */ (function () {
    function HomeController() {
        var _this = this;
        eel.expose(function () { return _this.clientPing(); }, 'clientPing');
        console.log('Calling eel.serverPing');
        eel.serverPing()().then();
    }
    HomeController.prototype.clientPing = function () {
        console.log('Pinged');
        eel.serverPing()().then();
    };
    return HomeController;
}());
var homeController;
eel.onInit(function () {
    homeController = new HomeController();
});
