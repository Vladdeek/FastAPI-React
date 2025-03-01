import React, { useState, useEffect } from 'react'
import CryptoCard from './components/crypto-card/crypto-card'

const App = () => {
	const [crypto, setCrypto] = useState([])

	// Функция для загрузки задач из FastAPI
	useEffect(() => {
		const fetchCrypto = async () => {
			try {
				const response = await fetch('/cryptocurrencies')
				const data = await response.json()

				// Проверяем структуру данных
				console.log('Ответ от сервера:', data)

				// Преобразуем данные в массив, если сервер возвращает объект
				const cryptoArray = Object.values(data) // Преобразуем объект в массив

				setCrypto(
					cryptoArray.map(coin => ({
						name: coin.name,
						price: coin.quote?.USD?.price,
						id: coin.id,
					}))
				)
			} catch (error) {
				console.error('Ошибка загрузки криптовалют:', error)
			}
		}

		fetchCrypto()
	}, []) // [] означает, что эффект сработает только при первом рендере

	return (
		<div className='container todo-con'>
			<div className='row todo-row'>
				{crypto && crypto.length > 0 ? (
					crypto.map((coin, index) => (
						<CryptoCard
							key={index}
							crypto={coin.name}
							cryptoPrice={coin.price}
						/>
					))
				) : (
					<p>Загрузка...</p>
				)}
			</div>
		</div>
	)
}

export default App
