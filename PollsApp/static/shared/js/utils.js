/**
 * Function add a css class to el HTMLElement, when time out
 * 
 * @param {HTMLElement} el Element to add class or classes
 * @param {number} time Timeout to trigger action
 */
function addClassByTimeOut(el, time) {
    setTimeout(() => el.classList.add('sidebar-transition'), time);
}

/**
 * Function that open a modal with page rendering by url
 * 
 * @param {*} url 
 * @param {*} id 
 */
function chargePageModalByURL(url, id){
    $(id).load(url, function(){
        $(this).modal('show');
    });
}

/**
 * Function that change the image in imgSelector, according to file selected in fileInputSelector
 * 
 * @param {*} param0
 */
function imagePreview({ imgSelector='', fileInputSelector='' }) {
    $(fileInputSelector).on('change', function() {
        const img = this.files[0];
        if (img) {
            let reader = new FileReader();
            reader.onload = function(event) {
                $(imgSelector).attr('src', event.target.result);
            }
            reader.readAsDataURL(img);
        }
    });
}