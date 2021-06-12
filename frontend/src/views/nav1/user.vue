<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px">
      <el-form :inline="true" :model="filters">
        <el-form-item>
          <el-input v-model="filters.name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" v-on:click="getUser">查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <template>
      <el-table
        :data="users"
        highlight-current-row
        v-loading="loading"
        style="width: 100%"
      >
        <el-table-column prop="id" label="id" width="120" sortable>
        </el-table-column>
        <el-table-column prop="nick" label="用户名" width="200" sortable>
        </el-table-column>
        <el-table-column prop="name" label="真实姓名" width="200" sortable>
        </el-table-column>
        <el-table-column prop="campus" label="校区" width="120" sortable>
        </el-table-column>
        <el-table-column prop="college" label="学院" width="200" sortable>
        </el-table-column>
        <el-table-column prop="major" label="专业" width="200" sortable>
        </el-table-column>
        <el-table-column prop="grade" label="年级" width="120" sortable>
        </el-table-column>
      </el-table>
    </template>
  </section>
</template>
<script>
import { getUserList } from "../../api/api";
import axios from "axios";
//import NProgress from 'nprogress'
export default {
  data() {
    return {
      filters: {
        name: "",
      },
      loading: false,
      users: [],
    };
  },
  methods: {
    //性别显示转换
    formatSex: function (row, column) {
      return row.sex == 1 ? "男" : row.sex == 0 ? "女" : "未知";
    },
    //获取用户列表
    getUser: function () {
      console.log("get user");
      let para = {
        name: this.filters.name,
      };
      this.loading = true;
      //   NProgress.start();
      getUserList(para).then((res) => {
        console.log(res.data);
        this.users = res.data;
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
    this.getUser();
  },
};
</script>

<style scoped></style>
