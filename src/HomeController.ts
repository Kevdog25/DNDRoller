declare var eel : any;

class HomeController {
    constructor(){
        eel.expose(() => this.clientPing(), 'clientPing')
        console.log('Calling eel.serverPing')
        eel.serverPing()().then()
    }

    private clientPing(){
        console.log('Pinged')
        eel.serverPing()().then()
    }
}

var homeController : HomeController;
eel.onInit(() => {
    homeController = new HomeController()
})