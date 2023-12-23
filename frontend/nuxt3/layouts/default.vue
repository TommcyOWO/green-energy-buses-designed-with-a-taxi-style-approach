<template>
  <div class="flex fixed w:100% jc:space-between font:medium">
    <div class="m:20px">
      <IconMenu2 @click="menu_toggle()" class="flex hide@>md" />
      <ul :class="{ 'hidden@<md': m_value }" class="list-style:none flex@>md f:20px">
        <li class="cursor:pointer m:10px f:semibold f:20px" @click="moveTo('index')">叫車服務</li>
        <li class="cursor:pointer m:10px f:semibold f:20px" @click="moveTo('bus_information')">公車資訊</li>
        <li class="cursor:pointer m:10px f:semibold f:20px" @click="moveTo('bus_stops')">公車站點</li>
        <!-- <li class="cursor:pointer m:10px f:semibold f:20px" @click="moveTo('bus_stops')">公車站點</li> -->
      </ul>
    </div>
    <div class="flex ai:center@>md px:10px {py:10px;rel}@<md text:center">
      <button v-if="authKey!=='null'" @click="sign_out()" class="btn mx:10 cursor:pointer">登出</button>
      <button v-else @click="moveTo('account-login')" class="btn mx:10 cursor:pointer">登入/註冊</button>
      <a href="https://github.com/TommcyOWO/taxi-style-green-energy-bus" target="_blank">
        <IconBrandGithub color="black" class="m:10" />
      </a>
    </div>
  </div>
  <slot />
</template>

<script setup lang="ts">
import { IconBrandGithub, IconMenu2 } from "@tabler/icons-vue";
import { init, Style } from '@master/css';
import Cookies from "cookies-ts"

Style.extend('classes', {
  btn: 'inline-flex center-content font:14 font:semibold b:2|solid font:black bg:white px:18 h:40 r:4',
  acinpu: 'h:30px w:205px shadow:0|1|black border:none outline:none',
  tselect:'my:5px h:25px b:2|solid bg:white outline:none r:4px'
})
init()
const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
const [m_value, menu_toggle] = useToggle(true);
const cookies = new Cookies();
const authKey = ref("null")

const sign_out = async () => {
  cookies.remove("auth_key")
  router.go(0)
}

onMounted(() => {
  try {
    const authCookie = cookies.get("auth_key");
    if (authCookie !== null) {
      authKey.value = authCookie;

    }
  } catch (error: any) {
    console.error(error);
  }
})
</script>
