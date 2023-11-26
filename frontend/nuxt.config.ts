// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr:false,
  modules:[
  '@nuxtjs/ionic'
  ,'@nuxtjs/i18n'],
  i18n: {
    vueI18n: './i18n/index.ts' // if you are using custom path, default 
  }
})
