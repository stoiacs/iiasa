
<template>
  <div class="carousel-container">
    <carousel :itemsToShow="1" :wrapAround="true" :navigationEnabled="true" :paginationEnabled="true">
      <slide v-for="n in 12" :key="n">
        <div class="carousel__item">
          <img :src="getImageSrc(n)" alt="Image" />
          <div class="title">{{ getMonthName(n) }}</div>
        </div>
      </slide>
      <template #addons>
        <Navigation />
        <Pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Navigation, Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css';

export default {
  components: {
    Carousel, Slide, Navigation, Pagination
  },
  methods: {
    getImageSrc(n) {
      const formattedNumber = n.toString().padStart(2, '0');
      return `img/wc2.1_30s_tavg_${formattedNumber}.tif.png`;
    },
    getMonthName(n) {
      const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
      return months[n - 1];
    }
  }
};
</script>

<style>
.carousel-container {
  max-width: 800px;
  height: 600px;
  margin: auto;
  position: relative;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

.title {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
}
</style>
