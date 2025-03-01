import React, { useState } from 'react'
import '../crypto-card/crypto-card.css'
import 'bootstrap/dist/css/bootstrap.min.css'

const CryptoCard = ({ crypto, cryptoPrice }) => {
	return (
		<div className='col-lg-4 col-md-6 col-xs-12'>
			<div className='content'>
				<div className='text'>
					<p className='name'>{crypto}</p>
					<p className='price'>{cryptoPrice}</p>
				</div>
			</div>
		</div>
	)
}

export default CryptoCard
