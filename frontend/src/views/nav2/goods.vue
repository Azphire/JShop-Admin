<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px">
      <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.id" placeholder="用户id"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getGood">查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <template>
      <el-table
        :data="goods"
        highlight-current-row
        v-loading="loading"
        style="width: 100%"
      >
        <el-table-column prop="sellerid" label="用户id" width="100" sortable>
        </el-table-column>
        <el-table-column prop="goodid" label="商品id" width="130" sortable>
        </el-table-column>
        <el-table-column prop="name" label="商品名" width="150" sortable>
        </el-table-column>
        <el-table-column prop="price" label="价格" width="100" sortable>
        </el-table-column>
        <el-table-column prop="description" label="描述" width="260" sortable>
        </el-table-column>
        <el-table-column prop="campus" label="校区" width="100" sortable>
        </el-table-column>
        <el-table-column prop="old" label="新旧" width="100" sortable>
        </el-table-column>
        <el-table-column prop="publishdate" label="日期" width="200" sortable>
        </el-table-column>
        <el-table-column prop="tag" label="标签" width="100" sortable>
        </el-table-column>
      </el-table>
    </template>
  </section>
</template>
<script>
import { getGoodList } from "../../api/api";
//import NProgress from 'nprogress'
export default {
  data() {
    return {
      filters: {
        name: "",
      },
      loading: false,
      goods: [],
    };
  },
  methods: {
    //获取列表
    getGood: function () {
      console.log("get good");
      let para = {
        id: this.filters.id,
      };
      this.loading = true;
      //   NProgress.start();
      getGoodList(para).then((res) => {
        console.log(res.data);
        this.goods = res.data;
        this.loading = false;
        //NProgress.done();
      });
      //   axios.get("http://127.0.0.1:5000/user/list").then((res) => {
      //     console.log("数据：", res.data);
      //     this.users = res.data;
      //     this.loading = false;
      //   });
    },
  },
  mounted() {
    this.getGood();
  },
};
</script>

<style scoped></style>
