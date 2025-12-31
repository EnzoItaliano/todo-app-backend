module.exports = (sequelize, Sequelize) => {
    const Task = sequelize.define("TaskItem", {
      title: {
        type: Sequelize.STRING
      },
      description: {
        type: Sequelize.STRING
      }
    });
  
    return Task;
};