odoo.define('duplex_fe.models', function(require) {
    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;

    ajax.jsonRpc('/dashboard/data', 'call', {
        'input_data': 'this is my input data',
        'param_1': 'param_1',
        'param_2': 'param_2',
        'param_3': 'param_3'
    }).then(function (data) {
        var output_data = data['groups']
        $("#output").html(output_data);
    });

    const WEEK = 'week';

    var DuplexDashboard = Widget.extend({
        template: 'duplex_fe.DuplexDashboard',
        events: {
            'click .js_link_analytics_settings': 'on_link_analytics_settings',
        },
        init: function(parent, context) {
            this._super(parent, context);
            this.date_range = WEEK;
            this.date_from = moment().subtract(1, WEEK);
            this.date_to = moment();
        }
    })
    core.action_registry.add('duplex_dashboard', DuplexDashboard);
    return DuplexDashboard;
});

