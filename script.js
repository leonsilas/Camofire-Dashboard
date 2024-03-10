function openSidebar() {
    document.getElementById('sidebar').style.width = '250px';
    document.getElementById('main').style.marginLeft = '250px';
    document.getElementById('footer').style.marginLeft = '250px';   
}

function closeSidebar() {
    document.getElementById('sidebar').style.width = '0';
    document.getElementById('main').style.marginLeft = '0';
    document.getElementById('footer').style.marginLeft = '0';
}

function toggleTheme() {
    var body = document.body;
    body.classList.toggle('dark-theme');
}