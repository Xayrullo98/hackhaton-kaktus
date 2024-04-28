let scrollUp = document.querySelector('.scroll-up')
scrollUp.addEventListener('click', (e)=>{
    e.preventDefault()
    window.scrollTo({ top: 0, behavior: 'smooth' });
})
function yuqoriga(item){
    document.querySelector(item).scrollIntoView({behavior: 'smooth'})
}