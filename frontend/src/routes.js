import Login from "./views/Login.vue";
import NotFound from "./views/404.vue";
import Home from "./views/Home.vue";
import Main from "./views/Main.vue";
import Table from "./views/nav1/Table.vue";
import Form from "./views/nav1/Form.vue";
import user from "./views/nav1/user.vue";
import Ask from "./views/nav4/ask.vue";
import Recommend from "./views/nav5/recommend.vue";
import echarts from "./views/charts/echarts.vue";
import Goods from "./views/nav2/goods.vue";
import Qiugou from "./views/nav3/qiugou.vue";
import GoodTable from "./views/nav2/GoodTable.vue";
import QiugouTable from "./views/nav3/QiugouTable.vue";
import AskTable from "./views/nav4/AskTable.vue";
import RecommendTable from "./views/nav5/RecommendTable.vue";

let routes = [
  {
    path: "/login",
    component: Login,
    name: "",
    hidden: true,
  },
  {
    path: "/404",
    component: NotFound,
    name: "",
    hidden: true,
  },
  //{ path: '/main', component: Main },
  {
    path: "/",
    component: Home,
    name: "管理用户",
    iconCls: "fa fa-id-card-o", //图标样式class
    children: [
      { path: "/main", component: Main, name: "主页", hidden: true },
      { path: "/usertable", component: Table, name: "管理" },
      { path: "/userinfo", component: user, name: "用户列表" },
    ],
  },

  {
    path: "/",
    component: Home,
    name: "管理商品",
    iconCls: "fa fa-shopping-bag",
    children: [
      { path: "/goodtable", component: GoodTable, name: "管理" },
      { path: "/goodinfo", component: Goods, name: "商品列表" },
    ],
  },

  {
    path: "/",
    component: Home,
    name: "管理好物求购",
    iconCls: "fa fa-comments",
    children: [
      { path: "/qtable", component: QiugouTable, name: "管理" },
      { path: "/qiugou", component: Qiugou, name: "好物求购列表" },
    ],
  },
  {
    path: "/",
    component: Home,
    name: "管理广场提问",
    iconCls: "fa fa-comments", //图标样式class
    children: [
      { path: "/atable", component: AskTable, name: "管理" },
      { path: "/ask", component: Ask, name: "广场提问列表" },
    ],
  },
  {
    path: "/",
    component: Home,
    name: "管理好物推荐",
    iconCls: "fa fa-comments", //图标样式class
    children: [
      {
        path: "/rtable",
        component: RecommendTable,
        name: "管理",
      },
      {
        path: "/recommend",
        component: Recommend,
        name: "好物推荐",
      },
    ],
  },
  {
    path: "/",
    component: Home,
    name: "可视化",
    iconCls: "fa fa-bar-chart",
    children: [{ path: "/echarts", component: echarts, name: "echarts" }],
  },
  {
    path: "*",
    hidden: true,
    redirect: { path: "/404" },
  },
];

export default routes;
