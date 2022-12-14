import React from 'react';
// import { makeStyles } from '@material-ui/core/styles';
// import Card from '@material-ui/core/Card';
// import CardContent from '@material-ui/core/CardContent';
// import CardMedia from '@material-ui/core/CardMedia';
// import Grid from '@material-ui/core/Grid';
// import Typography from '@material-ui/core/Typography';
// import Container from '@material-ui/core/Container';

// const useStyles = makeStyles((theme) => ({
// 	cardMedia: {
// 		paddingTop: '56.25%', // 16:9
// 	},
// 	link: {
// 		margin: theme.spacing(1, 1.5),
// 	},
// 	cardHeader: {
// 		backgroundColor:
// 			theme.palette.type === 'light'
// 				? theme.palette.grey[200]
// 				: theme.palette.grey[700],
// 	},
// 	postTitle: {
// 		fontSize: '16px',
// 		textAlign: 'left',
// 	},
// 	postText: {
// 		display: 'flex',
// 		justifyContent: 'left',
// 		alignItems: 'baseline',
// 		fontSize: '12px',
// 		textAlign: 'left',
// 		marginBottom: theme.spacing(2),
// 	},
// }));

const Authors = (props) => {
	const { authors } = props;
	if (!authors || authors.length === 0) return <p>Can not find any authors, sorry</p>;
	return (
		<React.Fragment>
			{/* <Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end"> */}
					{authors.map((author) => {
						return (
                            <div>
                                <h1>{author.author_id}</h1>
                                <h1>{author.lname}</h1>
                                <h1>{author.email_address}</h1>

                            </div>
							
						);
					})}
				{/* </Grid>
			</Container> */}
		</React.Fragment>
	);
};
export default Authors;