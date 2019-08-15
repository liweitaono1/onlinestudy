<template>
 <div class="shopping-cart-wrap">
    <h3 class="shopping-cart-tit">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <router-link :to="{ path: '/ShopCart' }">我的购物车</router-link> > 
        <router-link :to="{ path: '/Coupon' }">领券中心</router-link> > 
        <router-link :to="{ path: '/SettlePay' }">结算中心</router-link>
      </el-breadcrumb>
      <p>领券中心</p>
    </h3>
    <div class="row">
      <el-table ref="multipleTable" :data="coupons" tooltip-effect="dark" style="width: 100%">
        <el-table-column label="优惠券名" width="250">
          <template slot-scope="scope">
            <span>{{ scope.row.title}}</span>
          </template>
        </el-table-column>
        <el-table-column label="活动介绍" width="200">
          <template slot-scope="scope">
            <span>{{ scope.row.brief}}</span>
          </template>
        </el-table-column>

        <el-table-column prop="name" label="活动开始领取时间" width="212">
          <template slot-scope="scope">
            <span>{{scope.row.grant_begin_time}}</span>
          </template>
        </el-table-column>
        <el-table-column prop="address" label="优惠券生效时间" show-overflow-tooltip>
          <template slot-scope="scope">{{scope.row.start_time}}</template>
        </el-table-column>

        <el-table-column prop="address" label="优惠券有效期" show-overflow-tooltip>
          <template slot-scope="scope">{{scope.row.period}}</template>
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="120">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="getCupon(scope.$index, coupons)"
              type="text"
              size="small"
            >立即领取</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "Coupon",
  data() {
    return {
      coupons: []
    };
  },
  methods: {
    getCouponList() {
      this.$http.couponList().then(res => {
        this.coupons = Object.values(res.data);
      });
    },

    // 领取优惠券
    getCupon(index, rows) {
      let params = {
        coupon: rows[index].id
      };
      this.$http.coupon(params).then(res => {
        this.$message({
          message: ` ${res.data}`,
          center: true
        });
      });
    }
  },
  created() {
    this.getCouponList();
  }
};
</script>

<style lang="css" scoped>


.shopping-cart-wrap {
  width: 100%;
}
.shopping-cart-wrap h3,
.row {
  width: 1200px;
  margin: 0 auto;
}
.shopping-cart-wrap h3 {
  padding: 50px 0;
}


.el-breadcrumb {
  margin-left: 40px;
  width: 222px;
  color: #22c8c5;
}

.el-breadcrumb a {
  color: #409EFF;
}


.el-table .warning-row {
  background: #22c8c5;
}
.cell img {
  vertical-align: middle;
  width: 170px;
}
.cell a {
  color: #000;
  margin-left: 30px;
}
select {
  border: 0;
  outline: none;
  font-size: 12px;
  color: #666;
  line-height: 18px;
  width: 117px;
  height: 28px;
  padding-left: 16px;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
}
.total {
  width: 1200px;
  margin: 0 auto;
  margin-bottom: 82px;
  /*justify-content:flex-end;*/
}

.el-input {
  width: 600px !important;
  margin: 22px auto;
}

.el-breadcrumb {
  margin-left: 40px;
}
</style>
