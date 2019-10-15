<template>
  <header>
    <div class="text-box">
      <h1>吃货天堂 😋</h1>
      <p class="mt-3">制作我们喜爱的美食 ❤️ ️</p>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/recipes">
        查看食谱
        <span class="ml-2">&rarr;</span>
      </nuxt-link>
    </div>
  </header>
</template>

<script>
export default {
  head() {
    return {
      title: "首页"
    };
  }
};
</script>

<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(12, 5, 5, 0.4)
    ),
    url("/images/banner.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-family: cursive;
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
