const x = {
  dd: function () {
    console.warn('aaaa');
  },
};

const atom = {
  value: 1,

  addValue: function (value) {
    return atom.value + value;
  },
};

export default {
  a: () => 10,
  b: () => 20,
};
