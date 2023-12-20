let burgerIcon = document.querySelector('.burger-menu>i')
burgerIcon.onclick = (event) => {
    let burgerMenuBlock = document.querySelector('.burger-menu-block')
    burgerMenuBlock.classList.toggle('hide')
    if ( burgerIcon.classList.contains('fa-bars')){    burgerIcon.classList.remove('fa-bars')
    burgerIcon.classList.toggle('fa-xmark')
    } else {
        burgerIcon.classList.remove('fa-xmark')
        burgerIcon.classList.add('fa-bars')
    }
}
