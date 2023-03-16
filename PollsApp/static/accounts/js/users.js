const CollapseFilterSectionComponent = () => {
    return {
        filterOpen: Alpine.$persist(false).using(sessionStorage),
        button: {
            ['@click'](){
                this.filterOpen = !this.filterOpen;
            }
        },
        filter: {
            [':class'](){
                return this.filterOpen && 'show';
            },
        },
    }
}
