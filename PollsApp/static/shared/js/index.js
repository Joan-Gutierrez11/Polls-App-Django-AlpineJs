
/**
 *  Alpine Components
 */

const SidebarComponent = () => {
    return {
        openSidebar: Alpine.$persist(true).using(sessionStorage),
        init() {
            addClassByTimeOut(this.$el, 200);
        },
        toggle() {
            this.openSidebar = !this.openSidebar;
        },
        openCloseBehavior: {
            ['@toggle-sidebar.window'](){
                this.toggle();
            },
            [':class'](){
                return this.openSidebar && 'show';
            }
        }
    }
}

const ButtonToggleComponent = () => {
    return {
        toggleSidebar(){
            this.$dispatch('toggle-sidebar');
        },
        actionSidebarButton: {
            ['@click'](){
                this.toggleSidebar();
            }
        }
    }
}

const LogoutButton = () => {
    return {
        ['@click.throttle'](){
            sessionStorage.clear();
        }
    }
}
