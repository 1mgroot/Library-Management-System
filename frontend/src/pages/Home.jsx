import React from 'react';

import { Layout, Menu, Tabs, theme } from 'antd';
import RoomList from '../components/RoomList';
import ReservationList from '../components/ReservationList';
const { Header, Content, Footer, Sider } = Layout;

const items = [
    {
        key: "1",
        label:"Rooms",
    }
]
const Home = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const onClick = (e) => {
    console.log('click ', e);
  };

  return (
    <Layout hasSider>
      <Sider
        style={{
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
        }}
      >
        <div
          style={{
            height: 32,
            margin: 16,
            background: 'rgba(255, 255, 255, 0.2)',
          }}
        />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']} items={items} onClick={onClick}/>
      </Sider>
      <Layout
        className="site-layout"
        style={{
          marginLeft: 200,
        }}
      >
        <Header
          style={{
            padding: 0,
            background: colorBgContainer,
          }}
        />
        <Content
          style={{
            margin: '24px 16px 0',
            overflow: 'initial',
          }}
        >
          <div
            style={{
              padding: 24,
              textAlign: 'center',
              background: colorBgContainer,
            }}
          >
          <Tabs
                defaultActiveKey="1"
                // onChange={onChange}
                items={[
                {
                    label: `Room`,
                    key: '1',
                    children: <RoomList/>,
                },
                {
                    label: `Reservations`,
                    key: '2',
                    children: <ReservationList/>,
                },
                {
                    label: `Tab 3`,
                    key: '3',
                    children: `Content of Tab Pane 3`,
                },
                ]}
          />
          </div>
        </Content>
        <Footer
          style={{
            textAlign: 'center',
          }}
        >
        </Footer>
      </Layout>
    </Layout>
  );
};
export default Home;