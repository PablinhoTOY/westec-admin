<template>
    <div class="card">
      <h2>{{ t('home.welcome', {nombre: userStore.firstname}) }}</h2>
      <p>{{ $t("home.num_visits", 30) }}</p>
      <p>{{ $t("home.costo", { valor: $n(1456, "currencyFormat") }) }}</p>
      <p>{{ $d(new Date(), "longFormat") }}</p>

      </div>
  </template>
  <script>
    // Add this script:
    import { useI18n } from 'vue-i18n'
    import { useUserStore } from '../stores/user';

    export default {
  setup() {
    const userStore = useUserStore()
    const { t } = useI18n()

    return { userStore, t }
  }
}
  </script>
  <style>
  .order-card {
    color: #fff;
  }
  
  .bg-c-blue {
    background: linear-gradient(45deg, #4099ff, #73b4ff);
  }
  
  .bg-c-green {
    background: linear-gradient(45deg, #2ed8b6, #59e0c5);
  }
  
  .bg-c-yellow {
    background: linear-gradient(45deg, #ffb64d, #ffcb80);
  }
  
  .bg-c-pink {
    background: linear-gradient(45deg, #ff5370, #ff869a);
  }
  
  #inicio .card .card {
    border-radius: 5px;
    -webkit-box-shadow: 0 1px 2.94px 0.06px rgba(4, 26, 55, 0.16);
    box-shadow: 0 1px 2.94px 0.06px rgba(4, 26, 55, 0.16);
    border: none;
    margin-bottom: 30px;
    -webkit-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
  }
  
  #inicio .card .card .card-block {
    padding: 25px;
  }
  
  .order-card i {
    font-size: 26px;
  }
  
  .f-left {
    float: left;
  }
  
  .f-right {
    float: right;
  }
  </style>