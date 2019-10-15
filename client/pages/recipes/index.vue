<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>吃货天堂</h3>
          <nuxt-link to="/recipes/add" class="btn btn-info">添加食谱</nuxt-link>
        </div>
      </div>
      <template v-for="recipe in recipes">
        <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import RecipeCard from "~/components/RecipeCard.vue";

const sampleData = [
  {
    id: 1,
    name: "通心粉",
    picture: "/images/food-1.jpeg",
    ingredients: "牛肉, 猪肉, 羊肉",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 2,
    name: "羊肉串",
    picture: "/images/food-2.jpeg",
    ingredients: "牛肉, 猪肉, 羊肉",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 3,
    name: "炒饭",
    picture: "/images/banner.jpg",
    ingredients: "牛肉, 猪肉, 羊肉",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  }
];

export default {
  head() {
    return {
      title: "食谱列表"
    };
  },
  components: {
    RecipeCard
  },
  asyncData(context) {
    let data = sampleData;
    return {
      recipes: data
    };
  },
  data() {
    return {
      recipes: []
    };
  },
  methods: {
    deleteRecipe(recipe_id) {
      console.log(deleted`${recipe.id}`);
    }
  }
};
</script>

<style scoped>
</style>
