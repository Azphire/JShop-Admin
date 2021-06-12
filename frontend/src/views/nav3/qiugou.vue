<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px">
      <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.id" placeholder="用户id"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getPost">查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <template>
      <el-table
        :data="posts"
        highlight-current-row
        v-loading="loading"
        style="width: 100%"
      >
        <el-table-column prop="userid" label="用户id" width="120" sortable>
        </el-table-column>
        <el-table-column prop="title" label="标题" width="140" sortable>
        </el-table-column>
        <el-table-column prop="intro" label="详情" width="240" sortable>
        </el-table-column>
        <el-table-column prop="tag" label="标签" width="120" sortable>
        </el-table-column>
        <el-table-column prop="price" label="价格" width="140" sortable>
        </el-table-column>
        <el-table-column prop="campus" label="校区" width="120" sortable>
        </el-table-column>
        <el-table-column prop="condition" label="新旧" width="120" sortable>
        </el-table-column>
        <el-table-column prop="time" label="日期" width="180" sortable>
        </el-table-column>
      </el-table>
    </template>
  </section>
</template>
<script>
import { getQiugouList } from "../../api/api";
//import NProgress from 'nprogress'
export default {
  data() {
    return {
      filters: {
        name: "",
      },
      loading: false,
      posts: [],
    };
  },
  methods: {
    //获取列表
    getPost: function () {
      console.log("get qiugou");
      let para = {
        id: this.filters.postid,
      };
      this.loading = true;
      //   NProgress.start();
      getQiugouList(para).then((res) => {
        console.log(res.data);
        this.posts = res.data;
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
    this.getPost();
  },
};
</script>

<style scoped></style>
