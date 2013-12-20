openerp.web_menu_security = function(instance) {
    var Store = instance.web.Class.extend({
        init: function() {
            this.data = {};
        },
        get: function(key, _default) {
            if (this.data[key] === undefined) {
                var stored = localStorage[key];
                if (stored)
                    this.data[key] = JSON.parse(stored);
                else
                    return _default;
            }
            return this.data[key];
        },
        set: function(key, value) {
            this.data[key] = value;
            localStorage[key] = JSON.stringify(value);
        },
    });
    instance.web.ActionManager.include({

        init: function(parent) {
            this._super(parent);
            this.store = new Store();
            var self = this;
            var attributes = {
                'menu': {},
                'menu_all':{},
            };
            if (self.session.session_is_valid()){
                _.each(attributes, _.bind(function(def, attr) {
                    var to_set = {};
                    if(attr == 'menu_all'){
                        new instance.web.Model("ir.ui.menu").get_func("get_all_actions")(self.session.uid).pipe(function(res) {
                            self.set({'menu_all':res})
                        });
                    }
                    to_set[attr] = this.store.get(attr, def);
                    this.set(to_set);
                }, this));
           }
        },
        do_action: function(action, options) {
            var self = this
            var action = action
            if(self.session.session_is_valid()){
                access_action_list = []
                if(this.get('menu_all')){
                    access_action_list = this.get('menu_all')
                }
                if(access_action_list){
                    setTimeout(function () {
                        if (access_action_list){
                        if(($.inArray(action.id, access_action_list) != -1) && !(action.id === undefined) && action.target != 'new' && !action.report_rml){
                            alert("Not Authorised to view this page");
                            document.location.href="/";
                        }}
                }, 50);
                }
            }
            return this._super.apply(this, arguments)
        }
    });
}
