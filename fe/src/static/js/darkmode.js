(function (root) {
  function init() {
    check();

    document.querySelectorAll('#switch-dark-mode li').forEach(el => el.addEventListener('click', function (e) {
      e.preventDefault();
      let index = Array.prototype.indexOf.call(e.currentTarget.parentNode.children, e.currentTarget);

      (index == 0) ? set_light() : set_dark();
    }));
  };

  function check() {
    (localStorage.getItem('darkMode') == 'enabled') ? set_dark() : set_light();
    //console.log("echck")
  };

  function set_dark() {
    //console.log('darkmode')
    document.body.classList.remove('light-mode');
    document.body.classList.add('dark-mode');

    let toogler = document.getElementsByClassName('navbar-toggler-icon')
    if (toogler.length) toogler[0].classList.add('navbar-toggler-icon-black')

    //console.log(document.querySelectorAll('.cardMain .v-table'))
    document.querySelectorAll('.cardMain, .v-table').forEach(el => {
      el.classList.remove('v-theme--light')
      el.classList.add('v-theme--dark')
    })

    document.querySelectorAll('.v-table, .v-btn').forEach(el => {
      el.classList.remove('v-theme--light')
      el.classList.add('v-theme--dark')
    });

    localStorage.setItem('darkMode', 'enabled');
    localStorage.removeItem('lightMode');
  };

  function set_light() {
    //console.log('lightmode')
    document.body.classList.add('light-mode');
    document.body.classList.remove('dark-mode');

    let toogler = document.getElementsByClassName('navbar-toggler-icon')
    if (toogler.length) toogler[0].classList.remove('navbar-toggler-icon-black')

    document.querySelectorAll('.v-table, .v-btn').forEach(el => {
      el.classList.remove('v-theme--dark')
      el.classList.add('v-theme--light')
    });

    localStorage.setItem('lightMode', 'enabled');
    localStorage.removeItem('darkMode');
  };

  root.DARK_MODE = {
    set_dark: set_dark,
    set_light: set_light,
    init: init,
    check: check,
  };
})(window);

window.onload = window.DARK_MODE.init;