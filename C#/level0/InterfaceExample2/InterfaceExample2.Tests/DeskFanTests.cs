using Moq;

namespace InterfaceExample2.Tests
{
    public class DeskFanTests
    {
        [Fact]
        public void PowerLowerThanZero_OK()
        {
            var mock = new Mock<IPowerSupply>();
            mock.Setup(ps => ps.GetPower()).Returns(() => 0);
            var fan = new DeskFan(mock.Object);
            var expected = "Lower Power!";
            var actual = fan.Work();
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void PowerUpperThanZero_Warning()
        {
            var mock = new Mock<IPowerSupply>();
            mock.Setup(ps => ps.GetPower()).Returns(() => 220);
            var fan = new DeskFan(mock.Object);
            var expected = "Warning!";
            var actual = fan.Work();
            Assert.Equal(expected, actual);
        }
    }

    class PowerSupplyLowerThanZero: IPowerSupply
    {
        public int GetPower()
        {
            return 0;
        }
    }

    class PowerSupplyHigherThan200 : IPowerSupply
    {
        public int GetPower()
        {
            return 222;
        }
    }
}