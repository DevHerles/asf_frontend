odoo.duplex_fe = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.HomePage = instance.Widget.extend({
        start: function() {
            console.log("Duplex home page loaded");
        },
    });

    instance.web.client_actions.add('duplex_fe.dashboard_page', 'instance.duplex_fe.HomePage');
}
