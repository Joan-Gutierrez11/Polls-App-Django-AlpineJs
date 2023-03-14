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