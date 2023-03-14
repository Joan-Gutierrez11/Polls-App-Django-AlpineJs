
/**
 * Function that open a modal with page rendering by url
 * 
 * @param {*} url 
 * @param {*} id 
 */
function chargeDeleteModal(url, id){
    $(id).load(url, function(){
        $(this).modal('show');
    });
}
