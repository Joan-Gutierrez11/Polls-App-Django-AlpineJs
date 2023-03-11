function resizeHeightContent(selector, additionalSize = 0) {
    let remainHeight = $(window).innerHeight() - $('#top-navbar').height();
    let mainContentHeight = $('#wrapper-content > main div.container-fluid').innerHeight();

    if(mainContentHeight > remainHeight){
        $(selector).height(mainContentHeight + additionalSize);
        return;
    }

    $(selector).height(remainHeight);
}

function addTransitionClass(el, time) {
    setTimeout(() => el.classList.add('sidebar-transition'), time);
}

/**
 *  Alpine Components
 */

const SidebarComponent = () => {
    return {
        openSidebar: Alpine.$persist(true).using(sessionStorage),
        init() {
            addTransitionClass(this.$el, 200);
        },
        toggle() {
            this.openSidebar = !this.openSidebar;
        }
    }
}

const ButtonToggleComponent = () => {
    return {
        toggleSidebar(){
            this.$dispatch('toggle-sidebar');
        }
    }
}


/**
 * Main
 */

$(window).on({
    load: () => {
        resizeHeightContent('#wrapper-content');
        resizeHeightContent('#sidebar', 16);
    },
    resize: () => {
        resizeHeightContent('#wrapper-content');
        resizeHeightContent('#sidebar', 16);
    }
})
