

/*  we assume that jquery is installed */
$(document).ready(function() {

    /*console.log(document.location.pathname);*/
    //récupération du lien
    var place = '#'+document.location.pathname.split('/')[1];
    //$( '.navbar-nav' ).find( 'li.active' ).removeClass('active');
    $( place ).addClass( 'active' );
});
